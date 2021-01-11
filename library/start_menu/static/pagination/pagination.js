let count = document.querySelector('.all_data').children.length;
let cnt = 0; 
let type = document.querySelector('.all_data').dataset.type
if(type == 'book') {
    cnt = 5;
}
else {
    cnt = 15;
}
let cnt_page = Math.ceil(count / cnt); 


let paginator = document.querySelector(".paginator");
let page = "";
for (let i = 0; i < cnt_page; i++) {
  page += "<span data-page=" + i * cnt + "  id=\"page" + (i + 1) + "\">" + (i + 1) + "</span>";
}
paginator.innerHTML = page;


let div_num = document.querySelectorAll(".book_block_all_information");
for (let i = 0; i < div_num.length; i++) {
      div_num[i].style.display = "none";
  }
for (let i = 0; i < div_num.length; i++) {
  if (i < cnt) {
    div_num[i].style.display = "block";
  }
}

let main_page = document.querySelector(".all_data");
main_page.classList.add("paginator_active");

function pagination(event) {
  let e = event || window.event;
  let target = e.target;
  let id = target.id;
  
  if (target.tagName.toLowerCase() != "span") return;
  
  let num_ = id.substr(4);
  let data_page = +target.dataset.page;
  main_page.classList.remove("paginator_active");
  main_page = document.getElementById(id);
  main_page.classList.add("paginator_active");

  let j = 0;

  for (let i = 0; i < div_num.length; i++) {
    let data_num = div_num[i].dataset.num;
    if (data_num <= data_page || data_num >= data_page) {
      div_num[i].style.display = "none";
    }
  }
  for (let i = data_page; i < div_num.length; i++) {
    if (j >= cnt) break;
    div_num[i].style.display = "block";
    j++;
  }
}
