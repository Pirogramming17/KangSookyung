let minutes = 0;
let seconds = 0;
let mili = 0;
const appendmili = document.getElementById("mili");
const appendseconds = document.getElementById("seconds");
const appendminutes = document.getElementById("minutes");
const buttonstart = document.getElementById("btn_start");
const buttonstop = document.getElementById("btn_stop");
const buttonreset = document.getElementById("btn_reset");

const $btn_del = document.querySelector(".btn_del");
const $recordList = document.querySelector(".log");
const $allCheck = document.querySelector(".allcheckbox");

let intervalId;

buttonstart.onclick = function () {
  clearInterval(intervalId);
  intervalId = setInterval(operatetimer, 10);
};

buttonstop.onclick = function () {
  clearInterval(intervalId);

  let checkBox = document.createElement("input");
  checkBox.setAttribute("type", "checkbox");
  checkBox.setAttribute("class", "checkbox");
  let timeRecord = document.createElement("li");

  timeRecord.textContent =
    appendminutes.textContent +
    ":" +
    appendseconds.textContent +
    ":" +
    appendmili.textContent;

  $recordList.appendChild(checkBox);
  $recordList.appendChild(timeRecord);
};

function selectAll(selectAll) {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');

  checkboxes.forEach((checkbox) => {
    checkbox.checked = selectAll.checked;
  });
}

$allCheck.addEventListener("click", function () {
  selectAll(this);
});

buttonreset.onclick = function () {
  clearInterval(intervalId);
  mili = 0;
  seconds = 0;
  minutes = 0;
  appendmili.textContent = "00";
  appendseconds.textContent = "00";
  appendminutes.textContent = "00";
};

function operatetimer() {
  mili++;
  appendmili.textContent = mili > 9 ? mili : "0" + mili;
  if (mili > 99) {
    seconds++;
    appendseconds.textContent = seconds > 9 ? seconds : "0" + seconds;
    mili = 0;
    appendmili = "00";
  }
  if (seconds > 59) {
    minutes++;
    appendminutes.textContent = minutes > 9 ? minutes : "0" + minutes;
    seconds = 0;
    appendseconds = "00";
  }
}
