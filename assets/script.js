// Funkcja organizująca cookie
$(document).ready(function(){
    function getCookie(c_name) {
        if(document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if(c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if(c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start,c_end));
            }
        }
        return "";
    }
// Przechwytywanie tokenu csrf
    $(function () {
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            }
        });
    });
});
// Funkcja wysyłająca za pomocą Ajax'a dane to pliku views.py w momencie przesuwania elementów między kolumnami
document.querySelectorAll('.con').forEach((elem) => {
    new Sortable(elem, {
        group: 'shared',
        animation: 100,
        onAdd: (event) => {
            $.ajax({
                type: "POST",
                url:"/kanban/sort/",
                data:{
                    send_id:event.item.id,
                    end:event.to.id,
                },
            })
        }
    });
})
// Funkcja która po kliknięciu dodaje element do bazy danych
$('#add_task').click(function () {
    $.ajax({
        type:"POST",
        url:"/kanban/add/",
        data:{
            nazwa:$('#nazwa').val(),
            status:$('#status').val(),
        },
    })
})

// Funkcja która po kliknięcu 'x' na stronie usuwa element z bazy danych
document.querySelectorAll('#del').forEach((elem) => {
    elem.addEventListener('click', () => {
        elem.parentNode.parentNode.removeChild(elem.parentNode)
        $.ajax({
            url: "/kanban/delete/",
            type: "POST",
            data: { 
                elem_id: elem.parentNode.id
             }
        })
    })
})
