/* =========================================
   ChemAI Premium JavaScript
   static/js/main.js
========================================= */

document.addEventListener("DOMContentLoaded", () => {

    // -----------------------------
    // Fade Animation
    // -----------------------------

    document.querySelectorAll(".card").forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(25px)";

        setTimeout(() => {

            card.style.transition = "0.5s ease";

            card.style.opacity = "1";

            card.style.transform = "translateY(0px)";

        }, index * 120);

    });

    // -----------------------------
    // Search Box Auto Focus
    // -----------------------------

    const search = document.querySelector(
        'input[name="compound"]'
    );

    if (search) {

        search.focus();

    }

    // -----------------------------
    // AI Typing Effect
    // -----------------------------

    const ai = document.querySelector(".ai-answer");

    if (ai) {

        const fullText = ai.innerHTML;

        ai.innerHTML = "";

        let i = 0;

        function type() {

            if (i < fullText.length) {

                ai.innerHTML += fullText.charAt(i);

                i++;

                setTimeout(type, 8);

            }

        }

        type();

    }

    // -----------------------------
    // Copy SMILES
    // -----------------------------

    const smiles = document.getElementById("smiles");

    if (smiles) {

        smiles.addEventListener("click", () => {

            navigator.clipboard.writeText(
                smiles.innerText
            );

            alert("SMILES copied!");

        });

    }

    // -----------------------------
    // Scroll To Top
    // -----------------------------

    const topBtn = document.getElementById("topBtn");

    if (topBtn) {

        window.addEventListener("scroll", () => {

            if (window.scrollY > 300) {

                topBtn.style.display = "block";

            }

            else {

                topBtn.style.display = "none";

            }

        });

        topBtn.onclick = () => {

            window.scrollTo({

                top: 0,

                behavior: "smooth"

            });

        };

    }

    // -----------------------------
    // Card Hover
    // -----------------------------
    
    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.boxShadow =
                "0 0 30px rgba(37,99,235,.45)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.boxShadow = "";

        });

    });
    
// -----------------------------
// Theme Toggle
// -----------------------------

const themeCss = document.getElementById("theme-css");
const themeBtn = document.getElementById("themeToggle");

// Load saved theme
const savedTheme = localStorage.getItem("theme") || "dark";

themeCss.href = `/static/css/${savedTheme}.css`;

if(themeBtn){
    themeBtn.innerHTML = savedTheme === "dark" ? "☀️" : "🌙";

    themeBtn.addEventListener("click", ()=>{

        const current =
            themeCss.href.includes("dark.css")
            ? "dark"
            : "light";

        const next =
            current === "dark"
            ? "light"
            : "dark";

        themeCss.href = `/static/css/${next}.css`;

        localStorage.setItem("theme", next);

        themeBtn.innerHTML =
            next === "dark"
            ? "☀️"
            : "🌙";

        });

    }

});
// Floating AI

const bubble=document.getElementById("aiBubble");

const windowAI=document.getElementById("aiWindow");

const closeAI=document.getElementById("closeAI");

if(bubble){

    bubble.onclick=(e)=>{

        e.preventDefault();

        if (windowAI) {
            windowAI.style.display="block";

            windowAI.animate(

                [
                    {opacity:0,transform:"translateY(30px)"},
                    {opacity:1,transform:"translateY(0px)"}
                ],

                {
                    duration:250
                }

            );
        }

        if(closeAI){

            closeAI.onclick=()=>{

                if (windowAI) {
                    windowAI.style.display="none";
                }

            };

        }

    };

}
function showThinking(){

const chat=document.getElementById("chatMessages");

if(!chat) return;

const div=document.createElement("div");

div.className="ai-message";

div.id="thinking";

div.innerHTML="🤖 <i>ChemAI is thinking...</i>";

chat.appendChild(div);

chat.scrollTop=chat.scrollHeight;

}
function hideThinking(){

const t=document.getElementById("thinking");

if(t){

t.remove();

}

}

