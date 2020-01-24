// Syntax for Level 1: Automatic Table and Date Search (Required)

// read data.js and assign a variable to store the information
var alienData = data;

// Console.log to verify the the data has been stored
console.log(alienData);

// Define a function to obtain an array with the extract the values of the datetime and store in a variable
var dates = alienData.map(function(date) {
  return date.datetime;
});
  
// Extract unique values from the date array
const uniqueDates = [...new Set(dates)]
console.log(uniqueDates);


// Select the tag specific to add the data as a table in the html
var tbody = d3.select("tbody");

// Create an array with the column names for the table headers
var columns = ["datetime","city","state","country","shape","durationMinutes","comments"];

// Loop through the alienData and append each row to table on to the webpage using a function
function addTable(){
    alienData.forEach(aliens =>{
		// Creating the rows for each line
        var row = tbody.append("tr");
		// Creating the cells and appending values 
        columns.forEach(column => {
			// Formating the entries for City, State and Country to show them in upper case
            if(column =="city" || column =="state" ||column == "country"){
                row.append("td").text(aliens[column].toUpperCase());
              }
			  // Append the shape, duration and comment values
              else row.append("td").text(aliens[column]);    
        })
    })
}

// call the function to add the able to the html 
addTable();

// Capture the date entered in the filter input element (class "datetime")
var inputDate = d3.select("#datetime");

// Select the tag specific to the filter button on the html (class "filter-btn")
var filterButton = d3.select("#filter-btn");

// Select the tag specific to the reset the table button on the html (class "f#reset-btn")
var resetButton = d3.select("#reset-btn");

// Setting a function for filtering the data with the entered datetime value
function filterData(){

    // Prevent the webpage from refreshing
    d3.event.preventDefault();

    // Extract the value from the variable inputDate
    var Datevalue = inputDate.property("value");

    // Filter the data and assign it to a variable
    var filteredData = alienData.filter(function(date){
       return ((date.datetime === Datevalue ||Datevalue == "" )
            )
    })

    // Checking that the data has been filtered as expected
    console.log(filteredData);
	
    // Delete values of the original table containing all values 
    tbody.text("");
	
    // Update the table with the filtered data     
    filteredData.forEach(aliens =>{
        var row = tbody.append("tr");
        columns.forEach(column => {
            if(column =="city" || column =="state" ||column == "country"){
                row.append("td").text(aliens[column].toUpperCase())
              }
              else row.append("td").text(aliens[column]);   
        })
    })
}
// Add event handler for the click button to filter the table with the given input
filterButton.on("click",filterData);

// create a function for resetting the table 
function resetData(){
    tbody.text("");
    addTable();
    }
    
// Add event handler for the reset button to reset the table to original data 
resetButton.on("click",resetData);