async function fetch_site_map(site_map_url){
    try {
        const response = await fetch(site_map_url)
        const data = await response.json()
        return data
        
    } catch (error) {
        alert(error, response)
    }
}


async function set_navbar_links() {
    const navbar = document.querySelector(".navbar-nav")
    const navbar_map = await fetch_site_map("/site-map")
    console.log(navbar_map)
    navbar_map.forEach(item => {
        let key = item[0]
        let val = item[1]

        console.log(`${key} ==> ${val}`);
        const li_item = document.createElement("li")
        li_item.classList.add('nav-item')
    
        const a_item = document.createElement("a")
        a_item.classList.add('nav-link')
        a_item.href = key
        a_item.innerText = val
        li_item.appendChild(a_item)
        navbar.appendChild(li_item)
        
    });
    // <li class="nav-item">
    //     <a class="nav-link" href="{{link}}">{{name}}</a>
    // </li>
}

set_navbar_links()