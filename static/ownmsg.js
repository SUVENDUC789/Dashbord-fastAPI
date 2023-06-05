$(document).ready(function () {
    $('.copy-btn').click(function () {
        let mac = $(this).siblings('.copy-txt').text();
        $('.msg-alert').html(`<div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>${mac}</strong> copied successfully 😎
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>`);
    })
})