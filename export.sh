while getopts "v:" opt; do
    case "$opt" in
        v)
            FILE_PATH="$OPTARG"
            ;;
    esac
done

if [-z "$FILE_PATH" ]; then
    echo "No file path provided"
    exit 1
fi

export FILE_PATH

docker-compose up --build