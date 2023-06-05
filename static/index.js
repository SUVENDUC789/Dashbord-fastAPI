$(document).ready(function () {
    $('.copy-btn').click(function () {
        // console.log("click...")

        // console.log($(this).siblings('.copy-txt').text());

        let mac = $(this).siblings('.copy-txt').text();

        // let msg = document.getElementsByClassName('msg-alert');
        // msg.innerHtml

        let element = mac

        let inputElement = document.createElement('input')

        inputElement.setAttribute('value', element)

        document.body.appendChild(inputElement)

        inputElement.select();

        document.execCommand('copy')

        inputElement.parentElement.removeChild(inputElement)
    })
});