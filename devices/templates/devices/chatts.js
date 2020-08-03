var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, 
            {
                type: 'line',
                labels : ['red', 'blue', 'Yellow', 'Green', 'Purple', 'Orange'],
                data: {
                    datasets: [
                    {
                        label: 'A15j Humedad',
                        data: [2,5,4,89,45,45,24] ,
                        backgroundColor: [
                            'rgba(38, 221, 242, 0.2)'
                        ],
                        borderColor: [
                            'rgba(38, 221, 242, 1)'
                        ],
                        borderWidth: 1,
                        fill:false,
                        yAxisID:'y-axis-2',
                    },
                    {
                        label: 'L1a Humedad',
                        data: dat2,
                        backgroundColor: [
                            'rgba(56, 0, 211, 0.2)'
                        ],
                        borderColor: [
                            'rgba(56, 0, 211, 1)'
                        ],
                        borderWidth: 1,
                        fill:false,
                        yAxisID:'y-axis-2',
                    },
                    {
                        label: 'A15j Temperatura',
                        data: dat3,
                        backgroundColor: [
                            'rgba(0, 211, 24, 0.2)'
                        ],
                        borderColor: [
                            'rgba(0, 211, 24, 1)'
                        ],
                        borderWidth: 1,
                        fill:false,
                        yAxisID:'y-axis-1',
                    },
                    {
                        label: 'L1a Temperatura',
                        data: dat4,
                        backgroundColor: [
                            'rgba(247, 100, 27, 0.2)'
                        ],
                        borderColor: [
                            'rgba(247, 100, 27, 1)'
                        ],
                        borderWidth: 1,
                        fill:false,
                        yAxisID:'y-axis-1',
                    }]
                },
                options: {         
                    scales: {
                        yAxes: [{
                            type:'linear',
                            stacked: true,
                            position: 'right',
                            beginAtZaero:true,
                            id: 'y-axis-1',
                            ticks: {
                            suggestedMin: temin,
                            suggestedMax: tema,
                            },
                            scaleLabel:{
                                display:true,
                                labelString:'Temperatura'
                            }
                        },{
                            type:'linear',
                            stacked: true,
                            position: 'left',
                            beginAtZaero:true,
                            id: 'y-axis-2',
                            ticks: {
                            suggestedMin: humin,
                            suggestedMax: huma
                            },
                            scaleLabel:{
                                display:true,
                                labelString:'Humedad'
                            }
                        }],
                        
                    },
                    title:{
                        display:true,
                        text: "Grafico de camara"
                    }
                }
            
            });