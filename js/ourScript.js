document.getElementById('butt').addEventListener('click', function() {
            var searchContainer = document.getElementById('searchContainer');
            if (searchContainer.style.display === 'none') {
                searchContainer.style.display = 'block';
            } else {
                searchContainer.style.display = 'none';
            }
        });