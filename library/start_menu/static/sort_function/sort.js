document.querySelector('#decrease_sort').onclick = sortByDesc;
document.querySelector('#increase_sort').onclick = sortByAsc;

function sortByDesc() {
    let allBooks = document.querySelector('.all_data');
    for (let i = 0; i < allBooks.children.length; i++) {
        for (let j = i; j < allBooks.children.length; j++) {
            if(allBooks.children[i].getAttribute('data-sort') < allBooks.children[j].getAttribute('data-sort')) {
                replacedNode = allBooks.replaceChild(allBooks.children[j], allBooks.children[i]);
                insertAfter(replacedNode, allBooks.children[i]);
            }

        }
    }
}
function sortByAsc() {
    let allBooks = document.querySelector('.all_data');
    for (let i = 0; i < allBooks.children.length; i++) {
        for (let j = i; j < allBooks.children.length; j++) {
            if(allBooks.children[i].getAttribute('data-sort') > allBooks.children[j].getAttribute('data-sort')) {
                replacedNode = allBooks.replaceChild(allBooks.children[j], allBooks.children[i]);
                insertAfter(replacedNode, allBooks.children[i]);
            }

        }
    }
}

function insertAfter(element, refElement) {
    return refElement.parentNode.insertBefore(element, refElement.nextSibling);
}