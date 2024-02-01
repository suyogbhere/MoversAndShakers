$("#example").DataTable({ 
    //Datatables Configurations
    paging: true,
    pageLength: 10,
    lengthChange:false,
    autoWidth:true,
    searching:true,
    bInfo: true,
    bSort:true,

// BUTTONS
dom: 'lBfrtip',
buttons:[
    {   //COPY
        extend: 'copy',
        text: 'copy',
        className: 'btn btn-danger', 
        titleAttr: "Copy",

        // Choose the column you with to copy
        exportOptions:{
            columns:[0,1,2,3,4]
        }
    },
    {   //EXCEL
        extend: 'excel',
        text: 'excel',
        className: 'btn btn-danger',
        titleAttr: "Excel",

        // Choose the column you with to excel
        exportOptions:{
            columns:[0,1,2,3,4]
        }
    },
    {   //PRINT
        extend: 'print',
        text: 'print',
        className: 'btn btn-danger',
        titleAttr: "Print",

        // Choose the column you with to print
        exportOptions:{
            columns:[0,1,2,3,4]
        },
        // Font Size (when export to print)
        customize: function( win ) {
            $(win.document.body).css('font-size', '10pt')
            $(win.document.body).find('table')
            .addClass('compact')
            .css('font-size', 'inherit');
        }
    },   
    // {   //PDF
    //     extend: 'pdf',
    //     text: 'pdf',                            
    //     className: 'btn btn-secondary',
    //     titleAttr: "PDF",   

    //     // // Choose the column you with to pdf
    //     exportOptions:{
    //         columns:[0,1,2,3,4]
    //     },

    //     // center the table
    //     tableHearder:{
    //         alignment:'center'
    //     },

    //     // Font size and optimization
    //     customize: function(doc) {
    //         doc.styles.tableHearder.alignment = 'center'; //Header position
    //         doc.styles.tableBodyOdd.alignment = 'center'; //Body position1  (gray color)
    //         doc.styles.tableBodyEven.alignment = 'center'; //Header position2 (white color)
    //         doc.styles.tableHearder.fontSize = 7;          //header font-size
    //         doc.defaultStyle.fontSize = 6;                // body font-size
    //         // To get 100% width of the table \
    //         doc.content[1].table.widths = Array(doc.content[1].table.body[1]+length+ 1).join('*').split('');
    //     }
    // },   
]
});
