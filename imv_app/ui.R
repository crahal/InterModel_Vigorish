#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

shinyUI(fluidPage(

    # Application title
    titlePanel("IMV"),

    sidebarLayout(
        sidebarPanel(
            numericInput("ll1",
                         "Baseline model log likelihood:",
                         value = log(0.25)),
            numericInput("n1",
                        "Baseline model sample size:",
                        value = 50),
            numericInput("ll2",
                         "Enhanced model log likelihood:",
                         value = log(0.5)),
            numericInput("n2",
                         "Enhanced model sample size:",
                         value = 50),
            textOutput("imv_text")
        ),

        # Show a plot of the generated distribution
        mainPanel(
            plotOutput("distPlot")
        )
    )
))
