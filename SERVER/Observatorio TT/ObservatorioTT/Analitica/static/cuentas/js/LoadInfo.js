$(document).ready(function () {
    console.log("ready!");
    $("#id_Empresa").change(function () {
        var url = $("#movimientoForm").attr("data-proveedores-url");  // get the url of the `load_cities` vie

        var url2 = $("#movimientoForm").attr("data-cuentas-url");  // get the url of the `load_cities` view
        var proveedor = $(this).val();  // get the selected country ID from the HTML inputa

        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'proveedor': proveedor       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_provedores").html(data);  // replace the contents of the city input with the data that came from the server
            }
        });

        $.ajax({                       // initialize an AJAX request
            url: url2,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
            data: {
                'proveedor': proveedor       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_cuentas").html(data);  // replace the contents of the city input with the data that came from the server
            }
        });

    });


    $("#id_cuenta").change(function () {

            $("#btn-search").click();
        });


});


function confirmpayment(id, token) {
    alert(id)
    var url = id

    Swal.fire({
        title: '¿Estás seguro?',
        text: "Se confirmará el pago hecho",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Confirmado'
    }).then((result) => {
        if (result.value) {

            $.ajax({
                url: url,
                data: {
                    'csrfmiddlewaretoken': token
                },
                success: function (data) {
                    Swal.fire(
                        'Pago confirmado!',
                        'Tu pago ha sido confirmado',
                        'success'
                    )
                }
            });

        }
    })
}






