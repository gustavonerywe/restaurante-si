function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

document.addEventListener('DOMContentLoaded', function (){
    document.querySelectorAll('.remove').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-customer')
            console.log(id)
            var url = `/delete_customer/${id}/`
            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            })
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                console.log('data:', data);
                if(data.success){
                    document.getElementById('customer-' + id).remove();
                }
            });
        }
    })
})