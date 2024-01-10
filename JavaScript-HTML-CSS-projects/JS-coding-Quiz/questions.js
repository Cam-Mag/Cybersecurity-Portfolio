qst = document.querySelector("#questions");
btn = document.querySelectorAll("button");
timer = document.querySelector("#timer")
result = document.querySelector("#result")

var questions = [
  {
    title: "Commonly used data types DO NOT include:",
    choices: ["strings", "booleans", "alerts", "numbers"],
    answer: "alerts"
  },
  {
    title: "The condition in an if / else statement is enclosed within ____.",
    choices: ["quotes", "curly brackets", "parentheses", "square brackets"],
    answer: "parentheses"
  },
  {
    title: "Arrays in JAvascript can be used to store_________",
    choices: ["numbers and strings", "other arrays", "booleans", "all of the above"],
    answer: "all of the above"
  },
  {
    title: "Arrays are indicated using_________",
    choices: ["commas", "curly brackets", "brackets", "parentheses"],
    answer: "brackets"
  },

];

var time = questions.length * 20;
timer.textContent = time;

var count = 0;
var finish = false;
var interval;

initQuestion();
initTimer();

for (let i = 0; i < btn.length; i++) {
  btn[i].addEventListener('click', () => {
    let pick = btn[i].textContent
    console.log(pick)

    if (!finish) {
      if (pick === questions[count].answer) {
        result.textContent = "Correct!"
      } else {
        time -= 10;
        if (time < 0) {
          time = 0;
        }
        result.textContent = "Incorrect!"
      }

      setTimeout(() => {
        result.textContent = "";
      }, 250);

      count++;
      if (count < questions.length) {
        initQuestion();
      } else {
        finish = true;
        clearInterval(interval);
        localStorage.setItem('score', time)
        window.location = "score.html"
      }
    }
  });
}



function initQuestion() {
  qst.textContent = questions[count].title;
  for (let i = 0; i < questions[count].choices.length; i++) {
    btn[i].textContent = questions[count].choices[i];
  }
}

function initTimer() {
  interval = setInterval(function () {
    time--;
    timer.textContent = time;

    if (time === 0) {
      finish = true;
      clearInterval(interval);

      localStorage.setItem('score', time)
      window.location = "score.html"
    }
  }, 1000)
}