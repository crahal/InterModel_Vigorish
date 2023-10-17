#
# This is the server logic of a Shiny web application. You can run the
# application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)
library(ggplot2)

# Define server logic required to draw a histogram
shinyServer(function(input, output) {

    imv <- function(ll1, n1, ll2, n2) {
        a1 <- exp(ll1/n1)
        a2 <- exp(ll2/n2)
        getcoins <- function(a) {
            f <- function(p,a) abs(p*log(p)+(1-p)*log(1-p)-log(a))
            nlminb(.5,f,lower=0.001,upper=.999,a=a)$par
        }
        c1 <- getcoins(a1)
        c2 <- getcoins(a2)
        ew <- function(p1,p0) (p1-p0)/p0
        imv <- ew(c2,c1)
        return(imv)
    }

    output$imv_text <- reactive({
        paste0('IMV between baseline and enhanced models is ',
               imv(input$ll1, input$n1, input$ll2, input$n2))
    })

    output$distPlot <- renderPlot({

        likelihoods <- seq(0.001, 0.999, by=0.001)
        imvs <- c()

        for (i in seq_along(likelihoods)) {
            imvs[i] <- imv(input$ll1, input$n1, log(likelihoods[i]), input$n2)
        }

        d <- data.frame(ll <- log(likelihoods),
                        imv <- imvs)

        ggplot(d, aes(x = ll, y=imv)) +
            geom_vline(aes(xintercept = input$ll2), lty=2, color='black') +
            geom_hline(aes(yintercept = imv(input$ll1, input$n1, input$ll2, input$n2)), lty=2, color='black') +
            geom_line(color='dodgerblue1') +
            labs(x = 'Enhanced Model Log Likelihood',
                 y = 'IMV') +
            theme_bw()

    })

})
