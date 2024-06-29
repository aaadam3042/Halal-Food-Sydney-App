import LocationSearchBar from '@components/LocationSearchBar';
import { ServiceCard } from '@components/ServiceCard';
import RestaurantBanner from "@assets/RestaurantBanner.png"
import ButcherBanner from "@assets/ButcherBanner.png"

let restaurantServices = [
	{id:1, name: "Ahmad's Bakery", distance: '0.6', openTime:'4am-12pm', phone: '+61400000000', email: 'abcd@bc.com', halalStatus: 'Verified - Halal'}, 
	{id:2, name: 'Lakemba McDonalds', distance: '1.1', openTime:'9am-9pm', phone: '+61410111001', halalStatus: 'Partially Halal'},
	{id:3, name: "Bing Lee's Noodles", distance: '1.2', phone: '+61421880235', halalStatus: 'Confirmed - Halal'},
]

export function HomePage() {

  	return (
	<>	
		<LocationSearchBar />
		<ServiceCard title="Restaurants" services={restaurantServices} banner={RestaurantBanner} />
		<ServiceCard title="Butchers" services={restaurantServices} banner={ButcherBanner} />
	</>
  	);
}

export default HomePage;