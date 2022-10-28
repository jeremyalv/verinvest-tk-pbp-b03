function createCollection() {
    $.getJSON('/collection/json/', function(data) {
        // Empty the collection containers, if they contain any items
        $("#forumCollectionBody").empty();
        $("#edukasiCollectionBody").empty();
        
        let forumAmount = 0;
        let educationAmount = 0;

        // Count the number of forum and edukasi posts
        for (let i = 0; i < data.length; i++) {
            if (data[i].fields.post_type == 'forum') {
                forumAmount++;
            } else {
                edukasiAmount++;
            }


            // Append card item to appropriate collection
            let post_type = data[i].fields.post_type;
            let id = data[i].pk;
            let title = data[i].fields.title;

            let postItem =`<div class="p-6 mb-4 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md">
                <a href="/collection/${post_type}/${id}">
                    <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900">${title}</h5>
                </a>
                <p class="mb-3 font-normal text-gray-700 ">Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.</p>
                <a href="#" class="inline-flex items-center py-2 px-3 text-sm font-medium text-center text-white bg-primary rounded-lg hover:bg-primary focus:ring-4 focus:outline-none focus:ring-blue-300 ">
                    Read more
                    <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                </a>
            </div>`;
        }

    })
}