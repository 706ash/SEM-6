library(datasets)
data <- iris

repeat {
    
    cat("\n\n1. Head\n2. Structure\n3. Max\n4. Min\n5. Mean\n6. Median 1st and 3rd quartile\n7. Standard deviation and variance\n8. Summary\n9. Exit\n\nEnter your choice: ")
    choice <- as.integer(readline())

    if(!(choice %in% 1:9))
    {
        cat("\n\nInvalid choice!")
        next
    }

    if(choice %in% 3:7){
        name = readline("Enter the name of the column: ")
        if(!(name %in% colnames(data)))
        {
            print("Column not found!")
            next
        }
    }
    
    switch(
        choice,
        print(head(data)),
        print(str(data)),
        print(max(data[[name]])),
        print(min(data[[name]])),
        print(mean(data[[name]])),
        {
        print(paste("Median: ",median(data[[name]])))
        print(paste("1st Quartile: ",quantile(data[[name]], 0.25)))
        print(paste("3rd Quartile: ",quantile(data[[name]], 0.75)))
        },
        {
        print(paste("Standard Deviation: ",sd(data[[name]])))
        print(paste("Variance: ",var(data[[name]])))
        },
        print(summary(data)),
        {break},
    )

}

