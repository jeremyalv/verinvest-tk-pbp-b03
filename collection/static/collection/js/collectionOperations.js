// Run method
createCollection();
function createCollection() {
    

    $.getJSON(`${location.origin}/collections/json/`, function(data) {
        // Empty the collection containers, if they contain any items
        $("#forumCollectionBody").empty();
        $("#edukasiCollectionBody").empty();
        
        
        let forumAmount = 0;
        let educationAmount = 0;

        if (data.length != 0) {
            console.log("L: " + data.length);
        } else {
            console.log("DATA LENGTH 0")
        }

        console.log(data)
        // Count the number of forum and edukasi posts
        for (let i = 0; i < data.length; i++) {
            let post_type = data[i].fields.post_type;
            if (post_type == 'forum') {
                forumAmount++;
            } else {
                edukasiAmount++;
            }
            
            // Append card item to appropriate collection
            let id = data[i].pk;
            let title = data[i].fields.title;
            let username = data[i].fields.author[0];

            let viewers = data[i].fields.viewers;
            let upvotes = data[i].fields.upvotes;
            let comments_count = data[i].fields.comments_count;

            let postItem =`
            <div id="${post_type}Item-${id}" class="flex flex-col w-9/12 items-start p-6 mb-8 max-w-sm bg-white rounded-lg border border-gray-200 shadow-md hover:scale-103 md:hover:scale-105 hover:transition-all hover:ease hover:duration-300 hover:translate-y-1 hover:shadow-lg">
                <a href="#" class="mb-4 md:mb-8">
                    <h5 class="text-lg text-left md:text-xl font-medium tracking-tight text-gray-900">${title}</h5>
                </a>
                <div id="${post_type}Item-${id}-details" class="w-full flex flex-col items-start">
                    <div class="flex mb-2 font-normal text-gray-700">
                        <p class="mr-1 md:mr-1.5">by</p>
                        <div class="inline-block text-primary font-semibold">
                            ${username}
                        </div>
                    </div>

                    <div id="${post_type}Item-${id}-metrics" class="flex flex-row mb-4 md:mb-6"> 
                        <div id="${post_type}Item-${id}-metrics-views" class="flex justify-between mr-4">
                            <!-- View count -->
                            <p class="mb-3 font-bold text-gray-700 mr-1 md:mr-2">${viewers}</p>
                            <!-- View icon -->
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                                <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                            </svg>
                        </div>
                        <div id="${post_type}Item-${id}-metrics-upvotes" class="flex justify-between mr-4">
                            <!-- Upvote count -->
                            <p class="mb-3 font-bold text-gray-700 mr-1 md:mr-2">${upvotes}</p>
                            <!-- Upvote icon -->
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#E81A56" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M6.633 10.5c.806 0 1.533-.446 2.031-1.08a9.041 9.041 0 012.861-2.4c.723-.384 1.35-.956 1.653-1.715a4.498 4.498 0 00.322-1.672V3a.75.75 0 01.75-.75A2.25 2.25 0 0116.5 4.5c0 1.152-.26 2.243-.723 3.218-.266.558.107 1.282.725 1.282h3.126c1.026 0 1.945.694 2.054 1.715.045.422.068.85.068 1.285a11.95 11.95 0 01-2.649 7.521c-.388.482-.987.729-1.605.729H13.48c-.483 0-.964-.078-1.423-.23l-3.114-1.04a4.501 4.501 0 00-1.423-.23H5.904M14.25 9h2.25M5.904 18.75c.083.205.173.405.27.602.197.4-.078.898-.523.898h-.908c-.889 0-1.713-.518-1.972-1.368a12 12 0 01-.521-3.507c0-1.553.295-3.036.831-4.398C3.387 10.203 4.167 9.75 5 9.75h1.053c.472 0 .745.556.5.96a8.958 8.958 0 00-1.302 4.665c0 1.194.232 2.333.654 3.375z" />
                            </svg>                                      
                        </div>

                        <div id="${post_type}Item-${id}-metrics-comments" class="flex justify-between mr-4">
                            <!-- Comment count -->
                            <p class="mb-3 font-bold text-gray-700 mr-1 md:mr-2">${comments_count}</p>
                            <!-- Comment icon -->
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="#1B4BF5" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round" d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                        </div>
                    </div>
                </div>
                <div id="${post_type}Item-${id}-cta" class="self-center">
                    <a href="/collections/${post_type}/items/${id}/" class="inline-flex self-center w-max items-center py-2 px-3 md:py-3 md:px-6 text-sm font-medium text-center text-white bg-primary rounded-lg hover:bg-primary focus:ring-4 focus:outline-none focus:ring-blue-300 ">
                        View Post
                        <svg aria-hidden="true" class="ml-2 -mr-1 w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z" clip-rule="evenodd"></path></svg>
                        </a>
                    </div>
                </div>
            </div>`;
            
            // Append to respective collection
            $(`#${post_type}CollectionBody`).append(postItem);
        }
    });
}   

export { createCollection };