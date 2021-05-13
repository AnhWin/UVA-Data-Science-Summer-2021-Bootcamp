#Prompt: Write a program that asks the user to provide several inputs, and print them out.


#Multiple input, printing out as 1 list
{
month = readline(prompt="What month were you born? ")
day = readline(prompt="What day were you born? ")
year = readline(prompt="What year were you born? ")

paste("You were born on: ", month, day, ",", year)
}
