def safety_analysis(name):

    name = name.lower()

    database = {

        "benzene": {
            "Hazard Level": "High",
            "Flammable": "Yes",
            "Carcinogenic": "Yes",
            "Corrosive": "No",
            "Toxic": "Yes",
            "Advice": [
                "Use inside a fume hood.",
                "Avoid inhalation.",
                "Wear gloves and goggles.",
                "Keep away from flames."
            ]
        },

        "ethanol": {
            "Hazard Level": "Medium",
            "Flammable": "Yes",
            "Carcinogenic": "No",
            "Corrosive": "No",
            "Toxic": "Low",
            "Advice": [
                "Keep away from heat.",
                "Avoid drinking laboratory ethanol.",
                "Store in a closed container."
            ]
        }

    }

    return database.get(
        name,
        {
            "Hazard Level": "Unknown",
            "Flammable": "Unknown",
            "Carcinogenic": "Unknown",
            "Corrosive": "Unknown",
            "Toxic": "Unknown",
            "Advice": [
                "No safety information available."
            ]
        }
    )