 document.getElementById("btn").addEventListener("click", () => {
     document.querySelector(".wrapper").style.display = "block";
     document.querySelector("#btn").style.display = "none";
 })
 document.querySelector(".close").addEventListener("click", () => {
     document.querySelector(".wrapper").style.display = "none";
     document.querySelector("#btn").style.display = "block";
 })
