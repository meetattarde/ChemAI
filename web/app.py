from flask import Flask, redirect, render_template, request, session, redirect,send_file,flash
import sys
import os

sys.path.append(os.path.abspath(".."))

from services.safety_service import get_safety
from services.explanation_service import generate_explanation
from services.functional_group_service import get_group_information
from services.comparison_service import compare_compounds
from services.compound_service import get_compound_data
from services.reaction_engine import suggest_reactions
from services.similarity_engine import find_similar
from services.intelligence_engine import generate_reasoning
from services.reactivity_engine import analyze_reactivity
from services.ai_service import ask_ai
from services.learning.followups import get_followups
from services.learning.chat_title import generate_chat_title
from services.learning.progress import learning_progress
from services.daily_fact import get_daily_fact
from services.feedback_service import (
    initialize_feedback,
    save_rating,
    save_feedback,
    get_average_rating,
    total_ratings,
    get_feedback
)
from services.user_service import (
    initialize_users,
    create_user,
    login_user
)
from services.dashboard_service import get_dashboard
from services.user_service import (

    initialize_users,

    create_user,

    login_user,

    initialize_favorites,

    save_favorite,

    get_favorites

)
from services.activity_service import (
    initialize_activity,
    save_search,
    total_searches,
    explored_compounds
)
from services.user_service import remove_favorite
from services.pdf_service import create_report
from services.ai_chat import ask_ai
from database.user_manager import (get_recent_searches,add_recent_search,update_profile,verify_password)
from services.user_service import initialize_recent_searches

from api.pubchem_api import fetch_compound

from chemistry.properties import calculate_properties
from chemistry.functional_groups import detect_functional_groups
from chemistry.lipinski import lipinski_analysis
from chemistry.atom_counter import count_atoms
from chemistry.rings import ring_information
from chemistry.formula import molecular_formula
from chemistry.structure import generate_structure

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

app.secret_key = "chemai_secret"
initialize_feedback()
initialize_users()
initialize_favorites()
initialize_activity()
initialize_recent_searches()

print("Static folder:", app.static_folder)

@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")

@app.route("/search", methods=["GET", "POST"])
def home():
    compound = ""
    compound2 = ""
    comparison = None
    result = None

    reaction_options = []
    reaction_result = None
    selected_reaction = ""

    if request.method == "POST":

        compound = request.form.get("compound", "").strip().lower()
        compound2 = request.form.get("compound2", "").strip().lower()
        question = request.form.get("question", "").strip()
        selected_reaction = request.form.get("reaction", "")

        print("Compound entered:", compound)

        if compound:
            result = fetch_compound(compound)
            if "username" in session:
             add_recent_search(
             session["username"],
            compound
            )
            if "user" in session:
                save_search(session["user"], compound)

        if result:

            result["properties"] = calculate_properties(result["smiles"])
            result["groups"] = detect_functional_groups(result["smiles"])
            result["group_info"] = get_group_information(result["groups"])
            result["lipinski"] = lipinski_analysis(result["smiles"])
            result["atoms"] = count_atoms(result["smiles"])
            result["rings"] = ring_information(result["smiles"])
            result["formula2"] = molecular_formula(result["smiles"])

            result["image"] = generate_structure(
                result["smiles"],
                result["name"]
            )

            result["ai_explanation"] = generate_explanation(result["smiles"])

            result["safety"] = get_safety(result["name"])

            result["brain"] = generate_reasoning(result)

            result["reactivity"] = analyze_reactivity(result)

            result["similar"] = find_similar(result["smiles"])
            
            result["followups"] = get_followups(result)
            
            result["progress"] = learning_progress(result)

            reaction_options = suggest_reactions(result["smiles"])

            if selected_reaction:

                from services.reaction_service import get_reaction

                reaction_result = get_reaction(
                    compound,
                    selected_reaction
                )

                if reaction_result:
                    result["reaction_equation"] = reaction_result["equation"]

            # Ask ChemAI
            if question:
                study_mode = request.form.get("study_mode", "NCERT")
                explain_level = request.form.get("explain_level", "standard")
                result["ai_answer"] = ask_ai(result,
                                             question,
                                             study_mode,
                                                explain_level
                                                )
            result["chat_title"] = generate_chat_title(question)
            # Comparison
            if compound2:

                result2 = get_compound_data(compound2)

                if result2:

                    result2["properties"] = calculate_properties(result2["smiles"])
                    result2["groups"] = detect_functional_groups(result2["smiles"])
                    result2["lipinski"] = lipinski_analysis(result2["smiles"])
                    result2["atoms"] = count_atoms(result2["smiles"])
                    result2["rings"] = ring_information(result2["smiles"])
                    result2["formula2"] = molecular_formula(result2["smiles"])
                    result2["safety"] = get_safety(result2["name"])

                    comparison = compare_compounds(result, result2)

    return render_template(
        "index.html",
        result=result,
        compound=compound,
        compound2=compound2,
        comparison=comparison,
        reaction_options=reaction_options,
        selected_reaction=selected_reaction,
        reaction_result=reaction_result
    )

@app.route("/dashboard")
def dashboard():
    
    if "user" not in session:
        return redirect("/login")

    username = session.get("user")

    if not username:
        return redirect("/login")

    data = get_dashboard(username)
    
    favorites = get_favorites(username)
    
    recent_searches = get_recent_searches("username")
    
    return render_template(
        "dashboard.html",
        username=username,
        daily_fact=get_daily_fact(),
        data=data,
        favorites=favorites,
        recent_searches=recent_searches
    )
    
@app.route("/search", methods=["GET", "POST"])
def search():
    
    if "user" not in session:
        return redirect("/login")

    compound = request.args.get("compound", "")
    result = None

    if request.method == "POST":
        compound = request.form.get("compound", "").strip().lower()

    if compound:

        result = fetch_compound(compound)
        if "user" in session:

            save_search(session["user"], compound)

        if result:

            result["properties"] = calculate_properties(result["smiles"])
            result["groups"] = detect_functional_groups(result["smiles"])
            result["group_info"] = get_group_information(result["groups"])
            result["lipinski"] = lipinski_analysis(result["smiles"])
            result["atoms"] = count_atoms(result["smiles"])
            result["rings"] = ring_information(result["smiles"])
            result["formula2"] = molecular_formula(result["smiles"])
            result["image"] = generate_structure(
                result["smiles"],
                result["name"]
            )

            result["ai_explanation"] = generate_explanation(
                result["smiles"]
            )

            result["safety"] = get_safety(result["name"])

            result["brain"] = generate_reasoning(result)

            result["reactivity"] = analyze_reactivity(result)

            result["similar"] = find_similar(
                result["smiles"]
            )

    return render_template(
        "search.html",
        compound=compound,
        result=result
    )


@app.route("/chat")
def chat():
    return render_template("chat.html")

    if "user" not in session:
        return redirect("/login")

@app.route("/ask_ai", methods=["POST"])
def ai_chat():
    
    if "user" not in session:
        return redirect("/login")

    question = request.form.get("question")

    compound = request.form.get("compound")

    answer = ask_ai(question, compound)

    return jsonify({

        "answer": answer

    })


@app.route("/learn")
def learn():
    return render_template("learn.html")

    if "user" not in session:
        return redirect("/login")


@app.route("/about")
def about():
    return render_template("about.html")

    if "user" not in session:
        return redirect("/login")

@app.route("/community", methods=["GET", "POST"])
def community():
    
    if "user" not in session:
        return redirect("/login")

    success = None

    if request.method == "POST":

        action = request.form.get("action")

        if action == "rating":

            rating = request.form.get("rating")

            if rating:

                save_rating(int(rating))

                success = "⭐ Thank you for rating ChemAI!"

        elif action == "feedback":

            name = request.form.get("name", "").strip()

            email = request.form.get("email", "").strip()

            category = request.form.get("category", "Feedback")

            message = request.form.get("message", "").strip()

            if message:

                save_feedback(

                    name,

                    email,

                    category,

                    message

                )

                success = "🎉 Thank you! Your feedback has been submitted."

    return render_template(
        "community.html",
        success=success
    )
@app.route("/favorite/remove/<compound>")
def remove_favorite_route(compound):

    if "user" not in session:

        return redirect("/login")

    remove_favorite(

        session["user"],

        compound

    )

    return redirect("/dashboard")


@app.route("/admin")
def admin():

    average = get_average_rating()

    total = total_ratings()

    feedback = get_feedback()

    return render_template(

        "admin.html",

        average=average,

        total=total,

        feedback=feedback

    )
@app.route("/signup", methods=["GET", "POST"])
def signup():

    message = ""

    if request.method == "POST":

        username = request.form.get("username").strip()

        email = request.form.get("email").strip()

        password = request.form.get("password").strip()

        if create_user(username, email, password):

            return redirect("/login")

        else:

            message = "❌ Username or Email already exists."

    return render_template(

        "signup.html",

        message=message

    )
@app.route("/login", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        email = request.form.get("email").strip()

        password = request.form.get("password").strip()

        user = login_user(email, password)

        if user:

            session["user"] = user[1]

            return redirect("/dashboard")

        else:

            message = "❌ Invalid Email or Password."

    return render_template(

        "login.html",

        message=message

    )
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")
@app.route("/favorite/<compound>")
@app.route("/favorites")
def favorites():

    if "user" not in session:
        return redirect("/login")

    favorites = get_favorites(session["user"])

    return render_template(
        "favorites.html",
        favorites=favorites
    )
    
    return redirect(f"/search?compound={compound}")
    from flask import send_file
@app.route("/download/<compound>")
def download(compound):

    result = fetch_compound(compound)

    if not result:

        return "Compound not found"

    result["ai_explanation"] = generate_explanation(result["smiles"])
    result["safety"] = get_safety(result["name"])

    pdf = create_report(result)

    return send_file(

        pdf,

        as_attachment=True

    )
@app.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    return render_template("profile.html")

@app.route("/settings")

def settings():

    if "username" not in session:

        return redirect("/login")

    return render_template(

        "settings.html",

        username=session["username"],

        email=session["email"]

    )

@app.route("/update_profile", methods=["POST"])

def update_profile():

    if "username" not in session:

        return redirect("/login")

    username = request.form["username"]

    email = request.form["email"]

    update_profile(

    session["username"],

    username,

    email

)

    session["username"] = username

    session["email"] = email
    flash("Profile updated successfully")
    return redirect("/settings")

@app.route("/change_password", methods=["POST"])

def change_password():

    if "username" not in session:

        return redirect("/login")

    old_password = request.form["old_password"]

    new_password = request.form["new_password"]

    if not verify_password(session["username"], old_password):

        flash("Current password is incorrect!")

        return redirect("/settings")

    update_password(

        session["username"],

        new_password

    )

    flash("Password updated successfully!")

    return redirect("/settings")

if __name__ == "__main__":
     app.run(debug=True)