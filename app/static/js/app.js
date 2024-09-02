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

    document.querySelectorAll('.remove-category').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-category')
            console.log(id)
            var url = `/delete_category/${id}/`
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
                    document.getElementById('category-' + id).remove();
                }
            });
        }
    })

    document.querySelectorAll('.remove-item').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-item')
            console.log(id)
            var url = `/delete_item/${id}/`
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
                    document.getElementById('item-' + id).remove();
                }
            });
        }
    })

    document.querySelectorAll('.remove-role').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-role')
            console.log(id)
            var url = `/delete_role/${id}/`
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
                    document.getElementById('role-' + id).remove();
                }
            });
        }
    })

    document.querySelectorAll('.remove-employee').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-employee')
            console.log(id)
            var url = `/delete_employee/${id}/`
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
                    document.getElementById('employee-' + id).remove();
                }
            });
        }
    })

    document.querySelectorAll('.remove-table').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-table')
            console.log(id)
            var url = `/delete_table/${id}/`
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
                    document.getElementById('table-' + id).remove();
                }
            });
        }
    })

    document.querySelectorAll('.remove-reservation').forEach(function(button){
        button.onclick = function(){
            var id = this.getAttribute('data-reservation')
            console.log(id)
            var url = `/delete_reservation/${id}/`
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
                    document.getElementById('reservation-' + id).remove();
                }
            });
        }
    })
})