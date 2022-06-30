

// -----------------------CATEGORIES / INSPIRATION API--------------------------------

window.onload = function() {
    getMultipleAPIcalls();
};

// Create each recipe card for each API hit
function dipsplayCategoryResults(searchCategory, categorie) {
        searchCategory.hits.map(recipe=> {
        var recipeCard = document.createElement('div');
        recipeCard.classList.add('col-md-4');
        recipeCard.classList.add('col-md-6');
        recipeCard.classList.add('col-lg-4');
        recipeCard.innerHTML = 
              `  <a href="${recipe.recipe.url}" target="_blank">
                    <div class="card mb-4">
                        <div class="card-body">
                            <div class="image-container">
                                <img class="card-image"
                                src="${recipe.recipe.image}" alt="recipe image">
                            </div>
                            <h2 class="card-title">${recipe.recipe.label}</h2>
                            <hr />
                            <p class="card-bottom">
                                <small>Source: 
                                <span class="created-by">${recipe.recipe.source}</span>
                                </small>
                                </p>
                           </div>
                    </div>
                </div>
                </a>
    `;
    document.getElementsByClassName(`${categorie}-results`)[0].appendChild(recipeCard);
});
}

// MULTIPLE API CALLS FOR CATEGORIES:

async function getMultipleAPIcalls(recipeCard) {
    const categories = ["healthy", "vegetarian", "pastries", "light", "grilled", "meat", "fish", "kids"];
    const responses = await Promise.all(
	categories.map(async category => {
        let APP_ID = "2f1133a1";
        let API_KEY = "63872c307c1ea5bea9706e007963df6f";
        let response = await fetch(
            `https://api.edamam.com/search?app_id=${APP_ID}&app_key=${API_KEY}&q=${category}`
           
        );
        let searchCategory = await response.json();
        dipsplayCategoryResults(searchCategory, category);
	})
)
}
