function initMap() {
            // sets the starting configuration of the google map. Mainly disables a lot of unnecessary clutter.
            // set into a dark theme.
            var options = {
                center: {lat: 30, lng: -10},
                zoom: 2.8,
                zoomControl: true,
                zoomControlOptions:{
                    position: google.maps.ControlPosition.BOTTOM_CENTER
                },
                fullscreenControl: true,
                fullscreenControlOptions:{
                    position: google.maps.ControlPosition.BOTTOM_RIGHT
                },
                rotateControl: false,
                mapTypeControl: false,
                streetViewControl: false,
                scaleControl: false,
                styles: [
                    {elementType: 'water', stylers: [{color: "#444444"}]},
                    {elementType: 'labels', stylers: [{ visibility: "off"}]},
                    {
                        featureType: "poi",
                        elementType: "all",
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: "road",
                        elementType: "all",
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: "Transit",
                        elementType: "all",
                        stylers: [{visbility: "off"}]
                    },

                    {
                        featureType: 'administrative',
                        elementType: 'labels',
                        stylers: [{visibility: "off"}]
                    },
                    {
                        featureType: 'administrative',
                        elementType: 'geometry.stroke',
                        stylers: [{color: "#FFFFFF"}]
                    },
                    {
                        featureType: 'landscape',
                        elementType: 'all',
                        stylers: [{color: "#555555"}]
                    }
                ]
            };

            var map = new google.maps.Map(document.getElementById('map'), options);

            var newNews = {
                coords:{lat:42,lng:-72},
                content: '<a href=https://www.google.com>Google</a>'
            }

            var alertIcon = 'https://png.icons8.com/ios/10/91dc5a/sphere-filled.png';


            newsMarkers(newNews);

            function newsMarkers(news){
                var marker = new google.maps.Marker({
                    position:news.coords,
                    icon: alertIcon,
                    map:map
                });

                if(news.content){
                    var infoWindow = new google.maps.InfoWindow({
                        content:news.content
                    });
                    marker.addListener('click', function(){
                        infoWindow.open(map, marker);
                    });
                }
            }


        }