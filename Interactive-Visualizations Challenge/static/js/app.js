
// Defining the path to the json sample file
var path ="static/data/samples.json";

// Reading a function to read the file and initialize the dashboard

function init() {
    const data = d3.json(path).then(function(data) {    
    console.log(data);    

    // Define a variable that will contain all the labels in the dropdown menu 
    const labels = data.names;
     //d3.event.preventDefault();
     var dropdownMenu = d3.select("#selDataset");

     labels.forEach(name => { 
     //console.log(name);
     var option = dropdownMenu.append("option");
     option.text(name);
    });

 
    //Demography Info
    var metaData = data.metadata;
    // Reading and publishing the demographic information of the first label
    var metaData1 =(metaData[0])
     console.log(metaData1);
    var wfreq =metaData1.wfreq
     //console.log(wfreq);
    var demography = d3.select("#sample-metadata");
     demography.html(" ");
    Object.entries(metaData1).forEach(([key, value]) =>{
         var row = demography.append("h5");
         row.text(`${key} :  ${value}`)
        });

    // Charts

    // Bar chart of the top 10 OTU's of the selected ID label
    // Showing the first subject ID in the array

    var samples = data.samples
    //console.log(samples);
    var sample_values = samples.map(sample =>sample.sample_values);  
    //console.log(sample_values[0]);
    var top10sample_values = sample_values[0].slice(0,10).reverse();
    console.log(top10sample_values);
    var otu_ids = data.samples.map(sample =>sample.otu_ids); 
    var top10otu_ids = otu_ids[0].slice(0,10).reverse();
    
    var otu_labels = data.samples.map(sample =>sample.otu_labels);
    var top10otu_labels = otu_labels[0].slice(0,10).reverse();
    console.log(top10otu_labels);
    
    
    //Defining the data and bar chart layout (title)
    var barData =[{
        x:top10sample_values,
        y:top10otu_ids.map(id =>  ("OTU" + id.toString())),
        type:"bar",
        text:top10otu_labels,
        orientation: "h"
    }];

    var barLayout = {
        title: "Top 10 OTU's of the Subject"
    };


    Plotly.newPlot("bar", barData,barLayout); 

    // Gauge plot

    var gaugeData =[{
        domain:{x:[0,1],y:[0,1]},
        value:parseFloat(wfreq),
        title:{text: "Weekly washing Frequency"},
        type:"indicator",
        mode: "gauge+number",
        gauge: {axis:{range:[0,9]},
        steps:[
        {range:[0,1], color: "#DCDCDC"},
        {range:[1,2], color: "#A9A9A9"},
        {range:[2,3], color: "#808080"},
        {range:[3,4], color: "#8FBC8F"},
        {range:[4,5], color: "#3CB371"},
        {range:[5,6], color: "#9ACD32"},
        {range:[6,7], color: "#00FF7F"},
        {range:[7,8], color: "#32CD32"},
        {range:[8,9], color: "#6B8E23"},
        ]
        }
        }];

    var gaugeLayout = {
        width:700,
        height: 600, 
        margin: { t: 30, b: 50, l:100, r:100 } 
        };

    Plotly.newPlot("gauge",gaugeData, gaugeLayout);


    // Bubble Plot Chart

    var bubbleData =[{
        x: otu_ids[0],
        y: sample_values[0],
        text: otu_labels[0],
        mode: "markers",
        marker: {
        size: sample_values[0],
        color: otu_ids[0],
        colorscale: "Earth"}
    }];

    var bubbleLayout = {
        margin: { t: 0 },
        hovermode: "closests",
        xaxis: { title: "OTU ID"},
        yaxis: { title: "Sample Values"}
      };
  
    Plotly.plot("bubble", bubbleData, bubbleLayout);



    

 });
};

// Creating functions to update the dashboard based on the ID selected


function optionChanged(ID){    
    console.log(ID);
    updateDemography (ID);
    updatePlots(ID);
    updateGauge(ID);
};


// Updating demography section

function updateDemography(ID) {
    d3.json(path).then(function(data){
        var metaData = data.metadata;
        for (var i=0; i<metaData.length; i++) {
            if (metaData[i].id.toString() ===ID) {
                //console.log(metaData[i].id)    
                var demography = d3.select("#sample-metadata");
                demography.html(" ");
                Object.entries(metaData[i]).forEach(([key, value]) =>{
                var row = demography.append("h5");
                row.text(`${key} :  ${value}`);
                });
            };
        };
    });
};

// Updating bar and bubble charts

function updatePlots(ID) {
    //var ID= d3.select("#selDataset").property("value");
    d3.json(path).then(function(data) {
        var samples = data.samples 
          
    for (var i=0; i<samples.length; i++) {
        if (samples[i].id ===ID) {
            //console.log(samples[i].sample_values)
            
            let barData =[{
                x:samples[i].sample_values.slice(0,10).reverse(),
                y:samples[i].otu_ids.slice(0,10).map(id =>  ("OTU" + id.toString())).reverse(),
                type:"bar",
                text:samples[i].otu_labels.slice(0,10).reverse(),
                orientation: "h"
            }];

            let barLayout = {
                title: "Top 10 OTU's of the Subject"
            };
            Plotly.newPlot("bar", barData, barLayout);


            let bubbleData =[{
                x: samples[i].otu_ids,
                y: samples[i].sample_values,
                text: samples[i].otu_labels,
                mode: "markers",
                marker: {
                size: samples[i].sample_values,
                color: samples[i].otu_ids,
                colorscale: "Earth"}
            }];
        
            let bubbleLayout = {
                margin: { t: 0 },
                hovermode: "closests",
                xaxis: { title: "OTU ID"},
                yaxis: { title: "Sample Values"}
              };
          
        Plotly.plot("bubble", bubbleData, bubbleLayout);

        };
    };
});
};


// Updating the gauge chart section
function updateGauge(ID){
    d3.json(path).then(function(data){
        let metaData=data.metadata;
        for (var j=0; j<metaData.length; j++){
            if(metaData[j].id.toString() ===ID){
                let wfreq=metaData[j].wfreq;
                console.log(wfreq);
                var gaugeData =[{
                    domain:{x:[0,1],y:[0,1]},
                    value:parseFloat(wfreq),
                    title:{text: "Weekly washing Frequency"},
                    type:"indicator",
                    mode: "gauge+number",
                    gauge: {axis:{range:[0,9]},
                            steps:[
                            {range:[0,1], color: "#DCDCDC"},
                            {range:[1,2], color: "#A9A9A9"},
                            {range:[2,3], color: "#808080"},
                            {range:[3,4], color: "#8FBC8F"},
                            {range:[4,5], color: "#3CB371"},
                            {range:[5,6], color: "#9ACD32"},
                            {range:[6,7], color: "#00FF7F"},
                            {range:[7,8], color: "#32CD32"},
                            {range:[8,9], color: "#6B8E23"},
                            ]
                            }
                    }];
            
                var gaugeLayout = {
                    width:700,
                    height: 600, 
                    margin: { t: 30, b: 50, l:100, r:100 } 
                    };
            
                Plotly.newPlot("gauge",gaugeData, gaugeLayout);

                
            };
        };  
    });

}

// Call function to initialize the dashboard

init();
