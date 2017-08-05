var list = document.querySelector('#feed_list');


list.addEventListener("click", this.change_list.bind(this));


function change_list(e) {
    if (e.target.matches('.my_list') || e.target.matches('.desc') || e.target.matches('li>a')) {
        var selected = document.querySelector(".selected");
        selected.classList.remove("selected");
        if (e.target.matches('li>a')) {
            e.target.parentNode.classList.add("selected");
        } else if (e.target.matches('.my_list') || e.target.matches('.desc')) {
            e.target.parentNode.parentNode.classList.add("selected");
        }

    }
}



