from bing_image_downloader import downloader

queries = [
    "people with guns",
    "people with weapons",
    "man firing gun",
    "man or women with weapon",
    "gunfire",
    "mens and women with guns",
    "looting people",
    "robbery"
    "murder",
    "rape",
    "murderer and rapist"
    "group of people",
    "people gatherings",
    "protest",
    "people protesting"

]

for query in queries:
    try:
        downloader.download(
            query,
            limit=300,
            output_dir="dataset",
            adult_filter_off=True,
            force_replace=False,
            timeout=60,
            filter=filter,
            verbose=True,
        )
    except Exception as e:
        print(f"Error occured while downloading images for {query}")
        print("==============================================")
        print(e)
