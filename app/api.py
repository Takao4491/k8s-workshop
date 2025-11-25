import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Logique métier simplifiée pour le POC ---

# Base de données (simulée) des enchantements et leurs poids
ENCHANTMENTS = {
    "Sharpness": {"max_level": 5, "base_cost": 2},
    "Efficiency": {"max_level": 5, "base_cost": 1},
    "Protection": {"max_level": 4, "base_cost": 3},
}

# Base de données (simulée) des recettes simples
RECIPES = {
    "Diamond_Pickaxe": ["Diamond_x3", "Stick_x2"],
    "Enchanting_Table": ["Obsidian_x4", "Diamond_x2", "Book_x1"],
}


@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de santé."""
    return jsonify({"status": "OK", "service": "MCE-Utility API"}), 200


@app.route('/enchantment/cost', methods=['POST'])
def calculate_enchantment_cost():
    """Calcule le coût théorique d'un enchantement."""
    data = request.json
    item = data.get("item", "undefined")
    enchant_name = data.get("enchantment")
    level = data.get("level", 1)

    enchant = ENCHANTMENTS.get(enchant_name)

    if not enchant:
        return jsonify({"error": "Enchantment inconnu"}), 404
    
    if level > enchant['max_level']:
        return jsonify({"error": f"Niveau {level} dépasse le max de {enchant['max_level']}"}), 400

    # Formule simplifiée pour le POC : (coût de base * niveau) + 5
    cost = (enchant['base_cost'] * level) + 5
    
    result = {
        "item": item,
        "enchantment": enchant_name,
        "level": level,
        "cost_xp_levels": cost,
        "note": "Coût approximatif pour le POC (Minecraft Java)"
    }
    return jsonify(result), 200


@app.route('/recipe/validate', methods=['POST'])
def validate_recipe():
    """Valide si les ingrédients fournis correspondent à une recette connue."""
    data = request.json
    ingredients = set(data.get("ingredients", []))
    
    if not ingredients:
        return jsonify({"error": "Aucun ingrédient fourni"}), 400

    found_recipes = []
    
    for product, required_ingredients in RECIPES.items():
        required_set = set(required_ingredients)
        # Vérifie si tous les ingrédients requis sont présents
        if required_set.issubset(ingredients):
            found_recipes.append(product)
            
    if found_recipes:
        return jsonify({"success": True, "products_found": found_recipes, "message": "Recettes valides trouvées."}), 200
    else:
        return jsonify({"success": False, "message": "Aucune recette connue ne correspond à ces ingrédients."}), 200


if __name__ == '__main__':
    # Gunicorn sera utilisé en production (via Dockerfile), mais Flask en dev local
    app.run(debug=True, host='0.0.0.0', port=5000)
