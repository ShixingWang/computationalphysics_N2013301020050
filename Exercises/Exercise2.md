> Written with [作业部落](https://www.zybuluo.com/ShixingWang/note/303533)

# Exercise 2

## 

## 1. Install the Thesaurus_query Plugin on VIM

Many difficulties flushed when I tried to install this plguin. Now I will communicate briefly how I managed to intall it and provide possible solutions to the difficulties.

- Install Pathogen

Pathogen is a popular plugin manager famous for the simplicity in Windows environment, which was my first choice to manege the thesaurus_query plugin.

First download the code from [this website](http://www.vim.org/scripts/script.php?script_id=2332). You can also clone it from its [Github site](https://github.com/tpope/vim-pathogen), but I do not recommend for the often failure due to the <s> GFW </s> bad Internet connection.

Allocate the code in the last step into the path
`~/.vim/autoload`. Make the folder if there isn't such one.

For those who know nothing about `~/.vimrc`, create this file under the folder under your home folder.

`~/.vimrc` is a file defining some default settings of Vim. Using  this you can cutomize your vim and make it more convenient. More knowledge about `~/.vimrc` can be found on [this site](http://easwy.com/blog/archives/advanced-vim-skills-introduce-vimrc/).

Edit this file with Vim and write down this

> execute pathogen#infect()

> syntax on

> filetype plugin indent on

If `~/.vimrc` is not empty, just add one line 
 > execute pathogen#infect()
 
Pathogen is ready.

- Install Vundle

Vundle is another famous plugin manage. The phenomenonal plugin YouCompleteMe is managed by this manager. I installed this mainly because when I used Pathogen and installed thesaurus_query, there is no change on my VIM and I thought Pathogen did not work. However, nothing happened after installing the thesaurus_query plug in with Vundle, either. 

First to install the Vundle you can clone it from the Github using the following code in the terminal:

`git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim`

And in `~/.vimrc` add the following

>set nocompatible              " be iMproved, required

> filetype off                  " required


> " set the runtime path to include Vundle and initialize

> set rtp+=~/.vim/bundle/Vundle.vim

> call vundle#begin()

> " All of your Plugins must be added before the following line

> call vundle#end()            " required

> filetype plugin indent on    " required

> " To ignore plugin indent changes, instead use:

> " filetype plugin on

The details for installing is [here](https://github.com/VundleVim/Vundle.vim).

- Install Thesaurus_query Plugin

If you installed Pathegen, then

`git clone https://github.com/ron89/thesaurus_query.vim ~/.vim/bundle/thesaurus_query.vim`

and it _should_ be over.

If you installed Vundle, besides the step above, add this into your `~/.vimrc` between  `call vundle#begin()` and `call vundle#end()`

> Bundle 'ron89/thesaurus_query.vim '
 
And run VIM in the terminal, in the general mode, input `:PlugInstall`

And everything _should_ be ready.

Here is a screen shot showing I have installed the plugin with the plugin manager Vundle.

![2_4](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/2_4.png)

## 2.  Rewrite the README.md with VIM

Here is a [link](http://www.ccvita.com/487.html) to a simple guideline of VIM.

Here is a screen shot showing the editing window of VIM on Fedora.

![2_3](https://raw.githubusercontent.com/ShixingWang/computationalphysics_N2013301020050/master/Pictures/2_3.png)

Here is the link to the [README.md](https://github.com/ShixingWang/computationalphysics_N2013301020050/blob/master/README.md) file.


