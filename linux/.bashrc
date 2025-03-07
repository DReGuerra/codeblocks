# blocks to be added to .bashrc in $HOME

# export lammps executable to path
if [ -d "$HOME/lammps*/build" ] ; then
    PATH="$HOME/lammps*/build/:$PATH"
fi