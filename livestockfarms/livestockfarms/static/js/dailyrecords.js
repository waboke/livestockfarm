$(document).ready(function() {

    var loadForm = function() {
        var btn = $(this);
        $.ajax({
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function() {
                $(".modal-dailyrecords .modal-content").html("");
                $(".modal-dailyrecords").modal("show");
            },
            success: function(data) {
                $(".modal-dailyrecords .modal-content").html(data.html_form);
            }
        });
    };

    var saveForm = function() {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function(data) {
                if (data.form_is_valid) {
                    $("#dailyrecords-table tbody").html(data.html_product_list);
                    $(".modal-dailyrecords").modal("hide");
                } else {
                    $(".modal-dailyrecords .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    };


    /* Binding */
    $(".js-add-feeding").click(loadForm);
    $(".modal-dailyrecords").on("submit", ".js-add-feeding-form", saveForm);

    // Update product
    $(".dailyrecords-table").on("click", ".js-edit-feeding", loadForm);
    $(".modal-dailyrecords").on("submit", ".js-edit-feeding-form", saveForm);

    // Delete product
    $(".dailyrecords-table").on("click", ".js-delete-feeding", loadForm);
    $(".modal-dailyrecords").on("submit", ".js-delete-feeding-form", saveForm);

});