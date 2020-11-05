document.getElementById("btn").addEventListener("click", () => {
    document.querySelector(".wrapper").style.display = "block";
    document.querySelector("#btn").style.display = "none";
})

document.querySelector(".close").addEventListener("click", () => {
    document.querySelector(".wrapper").style.display = "none";
    document.querySelector("#btn").style.display = "block";
})

document.querySelector(".pay").addEventListener("click", () => {
    //document.querySelector(".loanResponse").style.display = "none";
    document.querySelector(".loanResponse").style.display = "block";
})



//import loanProfile_view from
/*

function handleClick(e) {
    e.preventDefault()
    if (onclick(e)=== true){
        {{response}}
    }else
    {
        window.location.reload(true)
    }

}
*/

