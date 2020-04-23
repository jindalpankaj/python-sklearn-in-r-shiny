library(shiny)
library(data.table)
library(reticulate)

source_python('nlp.py')


# Define UI for app that draws the line plot ----
ui <- fluidPage(
  # App title ----
  titlePanel("Predicting rating for a given hotel review."),
  # Sidebar layout with input and output definitions ----
  sidebarLayout(
    # Sidebar panel for inputs ----
    sidebarPanel(width = 6,
                 # Input: text box for writing review
                 textAreaInput(inputId = "inputText", 
                             label = "Write your hotel review:"),
                 submitButton(text = "Predict!")
    ),
    
    # Main panel for displaying outputs ----
    mainPanel(width = 6,
              # Output: Line Plot ----
              textOutput("predicted_rating")
    )
  ),
  
  hr(),
  
  fluidRow(
    column(12, helpText("This is a non-commercial project created for 
                        the purpose of self-learning. Code is available at 
                        https://github.com/jindalpankaj/python-sklearn-in-r-shiny. 
                        Prediction model was trained using data available 
                        at https://github.com/Thinkful-Ed/data-201-resources/raw/master/hotel-reviews.csv.
                        Last updated 23 April 2020."), 
           align = "center")
  )
)

# Define server logic required to draw the line plot ----

server <- function(input, output) {
  
  output$predicted_rating <- renderText({
    paste0("Predicted rating is: ", funcPredictRating(input$inputText), " out of 5.")
    }
  )
}

# running the app
shinyApp(ui = ui, server = server)