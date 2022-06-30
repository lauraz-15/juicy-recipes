
// -----------------------SEARCH AREA API--------------------------------


// Send API call based on user's input value
async function sendAPIcall() {

        let searchvalue = document.getElementById('text-value').value;

        let APP_ID = "2f1133a1";
        let API_KEY = "63872c307c1ea5bea9706e007963df6f";
        let response = await fetch(`https://api.edamam.com/search?app_id=${APP_ID}&app_key=${API_KEY}&q=${searchvalue}`);
        let searchData = await response.json();
        dipsplayResults(searchData);
    }

    function dipsplayResults(searchData) {
        searchData.hits.map(recipe=> {
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
                                src="${recipe.recipe.image}" alt="Image of a Recipe">
                            </div>
                            <h2 class="card-title">${recipe.recipe.label}</h2>
                            <hr />        
                            <p class="card-bottom">
                            <small>Source: 
                            <span class="created-by">${recipe.recipe.source}
                            </small></span> 
                            </p>
                        </div>
                    </div>
                </div>
                </a>
    `;
  document.getElementsByClassName('search-results')[0].appendChild(recipeCard);
});
 }

// Wait for the user to click the button
// send API call
function searchBtnClicked() {
    let searchBtn = document.getElementById('search-btn');
    searchBtn.addEventListener("click", ()=> {
        sendAPIcall();
        dipsplayResults(searchData);
        });
}

searchBtnClicked();

