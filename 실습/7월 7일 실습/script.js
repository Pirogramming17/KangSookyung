//Date 객체 생성
let date = new Date();

const makeCalendar = () => {
  const viewYear = date.getFullYear();
  const viewMonth = date.getMonth();

  //캘린더 년도 달 채우기
  document.querySelector(".year-month").textContent = `${viewYear}년 ${
    viewMonth + 1
  }월`;

  //이전 달 마지막 날짜 가져오기
  const prevLast = new Date(viewYear, viewMonth, 0);
  const prevDate = prevLast.getDate();
  const prevDay = prevLast.getDay();

  //이번 달 마지막 날짜 가져오기
  const thisLast = new Date(viewYear, viewMonth + 1, 0);
  const thisDate = thisLast.getDate();
  const thisDay = thisLast.getDay();

  //전체 달력에 필요한 날짜들을 만들어 주기 위한 배열
  const prevDates = [];
  const thisDates = [...Array(thisDate + 1).keys()].slice(1);
  const nextDates = [];

  //prevDates 계산
  if (prevDay !== 6) {
    for (let i = 0; i < prevDay + 1; i++) {
      prevDates.unshift(prevDate - i);
    }
  }

  //nextDates 계산
  for (let i = 1; i < 7 - thisDay; i++) {
    nextDates.push(i);
  }

  //Dates 합치기
  const dates = prevDates.concat(thisDates, nextDates);
  const firstDateIndex = dates.indexOf(1); //5
  const lastDateIndex = dates.lastIndexOf(thisDate); //35

  //확인해봅시다
  console.log(firstDateIndex);
  console.log(lastDateIndex);

  dates.forEach((date, i) => {
    const condition =
      i >= firstDateIndex && i < lastDateIndex + 1
        ? "this" // true일 경우
        : "other"; // flase일 경우

    dates[
      i
    ] = `<div class="date"><span class="${condition}">${date}</span></div>`;
  });

  //dates 날짜 html 그리기
  document.querySelector(".dates").innerHTML = dates.join("");

  //오늘 날짜 체크하기
  const today = new Date();
  if (viewMonth === today.getMonth() && viewYear === today.getFullYear()) {
    for (let date of document.querySelectorAll(".this")) {
      if (+date.innerText === today.getDate()) {
        date.classList.add("today");
        break;
      }
    }
  }
};

//바로 함수 실행하여 이번 달 함수 그리기
makeCalendar();

//이전 달 그리기
const prevMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() - 1);
  makeCalendar();
};

//다음 달 그리기
const nextMonth = () => {
  date.setDate(1);
  date.setMonth(date.getMonth() + 1);
  makeCalendar();
};

//현재 달 그리기
const curMonth = () => {
  date = new Date();
  makeCalendar();
};
