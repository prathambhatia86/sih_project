const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");

const optionsList = document.querySelectorAll(".option");

selected.addEventListener("click", () => {
  optionsContainer.classList.toggle("active");
});

optionsList.forEach(o => {
  o.addEventListener("click", () => {
    selected.innerHTML = o.querySelector("label").innerHTML;
    optionsContainer.classList.remove("active");
  });
});
const selected1 = document.querySelector(".selected");
const options1Container1 = document.querySelector(".options-container");

const options1List1 = document.querySelectorAll(".option");

selected1.addEventListener("click", () => {
  options1Container1.classList1.toggle("active");
});

optionsList.forEach(o => {
  o.addEventListener("click", () => {
    selected1.innerHTML = o.querySelector("label").innerHTML;
    optionsContainer1.classList1.remove("active");
  });
});