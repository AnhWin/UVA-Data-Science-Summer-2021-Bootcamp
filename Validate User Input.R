#if not already installed, install qDap
#install.packages("qdap")

library(qdapDictionaries)
is.word  <- function(x) x %in% GradyAugmented

{cword <- readline(prompt="Please type a word: ")

#is.word(c(cword))

if (is.word(c(cword)))
{paste(cword, 'is an English word')
} else
{paste(cword, 'is not an English word')
}
}
