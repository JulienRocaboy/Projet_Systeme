for fichier in intensite.py recherche_plot.py; do
    if [ ! -f "$fichier" ]; then
        printf 'Erreur : fichier requis absent du dossier courant'
        exit 1
    fi
done


python3 intensite.py "$@"
python3 recherche_plot.py