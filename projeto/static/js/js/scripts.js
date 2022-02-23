
$(document).ready(function(){

    $('.form-group').addClass('col-md-4');
    $('#div_id_tutorial').addClass('col-md-12');
    $('.asteriskField').css('color', 'red')
    $('label').css('color', 'black')
    //$('span').addClass('text-uppercase')
    $('#id_dataIni, #id_dataFim').attr('type', 'date');
    $('#div_id_observacao').addClass('col-md-8');
    $('th').css('color', 'black')
    $('td').css('color', 'black')
   
    //Carregar os Formulários
   
    var table = $('#dataListagens').DataTable({
        language: {
            "emptyTable": "Nenhum registro encontrado",
            "info": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 até 0 de 0 registros",
            "infoFiltered": "(Filtrados de _MAX_ registros)",
            "infoThousands": ".",
            "loadingRecords": "Carregando...",
            "processing": "Processando...",
            "zeroRecords": "Nenhum registro encontrado",
            "search": "Pesquisar",
            "paginate": {
                "next": "Próximo",
                "previous": "Anterior",
                "first": "Primeiro",
                "last": "Último"
            },
            "aria": {
                "sortAscending": ": Ordenar colunas de forma ascendente",
                "sortDescending": ": Ordenar colunas de forma descendente"
            },
        },
        lengthChange: false,
        fixedColumns: false,
        "scrollX": true,
        buttons:[
            {
                extend: 'copy',
                text: "<i class='far fa-copy'></i> Copiar"
            },
            {
                extend: 'pdf',
                text:"<i class='far fa-file-pdf'></i> PDF"
            },
            {
                extend: 'excel',
                text: "<i class='far fa-file-excel'></i> Excel"

            },
            {
                extend: 'print',
                text: "<i class='fas fa-print'></i> Imprimir"

            }
        ]
    });
    table.buttons().container()
        .appendTo('#dataListagens_wrapper .col-md-6:eq(0)'
    );

    var str = "";
    str += " <div class='input-group my-2 mx-0'>";
    str += " <input type='text' id='myInput' class='form-control'>";
    str += " <div class='input-group-append'>";
    str += "  <button class='btn btn-secondary' type='button'id='button-addon2' disabled><i class='fas fa-search'></i></button>";
    str += "  </div>";
    str += "  </div>";

    $('.dt-buttons ').addClass("m-0");

    $('#dataListagens_filter > label').hide();
    $('#dataListagens_filter').append(str);

    $('#myInput').on( 'keyup', function () {
        table.search( this.value ).draw();
    } );
    
    $('button.buttons-html5').removeClass("btn-secondary");
    $('button.buttons-colvis').removeClass("btn-secondary");
    $('button.buttons-print').removeClass("btn-secondary");
    $('button.buttons-html5').addClass("btn-outline-secondary");
    $('button.buttons-print').addClass("btn-outline-secondary");
    $('button.buttons-colvis').addClass("btn-outline-secondary");  

    $('div.dt-buttons').addClass("my-2");  
    $('[data-toggle="tooltip"]').tooltip();

    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
      })

    
});        