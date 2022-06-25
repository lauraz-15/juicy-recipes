
// -----------------------SEARCH AREA API--------------------------------

function searchBtnClicked() {
    let searchBtn = document.getElementById('search-btn')
    searchBtn.addEventListener("click", ()=> {
        sendAPIcall();
        dipsplayResults(searchData)
        })
}

searchBtnClicked()

async function sendAPIcall() {

        let searchvalue = document.getElementById('text-value').value

        let APP_ID = "2f1133a1"
        let API_KEY = "63872c307c1ea5bea9706e007963df6f"
        let response = await fetch(`https://api.edamam.com/search?app_id=${APP_ID}&app_key=${API_KEY}&q=${searchvalue}`);
        console.log(response)
        let searchData = await response.json()
        console.log(searchData);
        console.log(`${searchData.hits[0].recipe.label}`)
        dipsplayResults(searchData)
        console.log(`Search value is: ${searchvalue}`)
        console.log(searchData.hits)
    }

    function dipsplayResults(searchData) {
        searchData.hits.map(recipe=> {
        var recipeCard = document.createElement('div');
        recipeCard.classList.add('col-md-4')
        recipeCard.innerHTML = 
              `  <a href="${recipe.recipe.url}" target="_blank">
                    <div class="card mb-4">
                        <div class="card-body">
                            <div class="image-container">
                                <img class="card-image"
                                src="${recipe.recipe.image}">
                            </div>
                            <h2 class="card-title">${recipe.recipe.label}</h2>
                            <hr />
                            <small>
                                <p class="card-bottom">Source: 
                                <span class="created-by">${recipe.recipe.source}</span>
                                </p>
                            </small>
                        </div>
                    </div>
                </div>
                </a>
    `
  document.getElementsByClassName('search-results')[0].appendChild(recipeCard);
})
 }



