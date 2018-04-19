#Hackathon Spring 2018 
#Deep Geeks 
#Opioid Overdoses and Deaths in US
#application by clicking 'Run App' above.
#

require(shiny)
require(googleVis)
require(plotly)


#Load overdose data 

overdose_states <- read.csv("./VSRR_Provisional_Drug_Overdose_Death_Counts.csv", header = T)
overdose_states <- overdose_states[c(-1, -4, -5, -8, -9, -10)]


library(shiny)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {
   
    # function to store stat type
    displayYear <- reactive({
        input$Year
    })
    stat_type <- reactive({
            input$statType
    })
    
    
    # Reactive label for the choropleth
    output$mapYear <- renderText({
        stat <- stat_type()
        
       if (stat == "DataValue") {
            paste("Total Opioid Overdose and Deaths in", displayYear())
        }
    })
    
    # Reactive label for the data table
    output$tableYear <- renderText({
        paste("Opioid Overdose and/or Statistics for the Year", displayYear())
    })
    
    # reactive function that subsets the data based on slider and radio buttons
    df_subset <- reactive({
        data <- overdose_states[(overdose_states$Year == displayYear() & overdose_states$Indicator == input$odType),]
        
        return(data)
    })
    
   
    
    # Reactive Choropleth map that changes based on radio button/slider selections
    output$choropleth <- renderGvis({
        data <- df_subset()
        stat <- stat_type()
    
        gvisGeoChart(data, "StateName", stat, options = list(region="US",
                                                             displayMode = "regions",
                                                             resolution = "provinces",
                                                             colors = "['#fff7f3', '#fde0dd', '#fcc5c0', '#fa9fb5',
                                                                  '#f768a1', '#dd3497', '#ae017e', '#7a0177', '#49006a']",
                                                             width = 500, 
                                                             height = 300))
    })
    
    ### Create table that outputs data based on selected radio buttons
    output$myTable <- renderGvis({
        data <- df_subset()
        gvisTable(data, options= list( width=550,height= 275), formats = list(Year = "####"))         
    })
  
})
