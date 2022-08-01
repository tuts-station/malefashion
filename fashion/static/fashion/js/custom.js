$('.plus-cart').click(function () {
    var id = $(this).attr("pid");
    var eml = $(this);
    $.ajax(
        {
            type: "GET",
            url: "/pluscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                $('.quantity-val').val(data.quantity)
                $('#amount').text('$ ' + data.amount);
                $('#totalamount').text('$ ' + data.totalamount);
            }
        })
});

$('.minus-cart').click(function () {
    var id = $(this).attr("pid");
    var eml = $(this);
    $.ajax(
        {
            type: "GET",
            url: "/minuscart",
            data: {
                prod_id: id
            },
            success: function (data) {
                $('.quantity-val').val(data.quantity)
                $('#amount').text('$ ' + data.amount);
                $('#totalamount').text('$ ' + data.totalamount);
            }
        })
});

$('.remove-cart').click(function () {
    var id = $(this).attr("pid");
    var elm = this;
    $.ajax(
        {
            type: "GET",
            url: '/removecart',
            data: {
                prod_id: id
            },
            success: function (data) {
                console.log(data);
                elm.parentNode.parentNode.parentNode.remove();
                document.getElementById("amount").innerText = data.amount;
                document.getElementById("totalamount").innerText = data.totalamount;
            }
        })
});

$('body').on('click','.add-favourite',function (argument) {
    id = $(this).data("id");
    // var img2 = $('.white-heart').data("img");
    // $('.white-heart').attr("src", img2);
    $.ajax({
        type: "GET",
        url: `/product/${id}/favourites`,
        success: function (data) {
            console.log("Success");
        },
    });
})
