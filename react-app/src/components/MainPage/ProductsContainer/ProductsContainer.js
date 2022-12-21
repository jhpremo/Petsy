import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useLocation, NavLink } from "react-router-dom";
import { getProducts } from "../../../store/items";
import Product from "../Product/Product";
import slidingWindowPages from "./utils/slidingWindowPages"

import "./ProductsContainer.css";

export default function ProductsContainer({ isSearch }) {
    const [numResults, products] = useSelector(state => [state.items.numResults, state.items] || 60)
    const [randomPage] = useState((Math.floor(Math.random() * 100) % 5) + 1)
    const [page, setPage] = useState(1);
    const [pageNums, setPageNums] = useState([])
    const [displayPageNums, setDisplayPageNums] = useState([])
    const [prefix, setPrefix] = useState(false)
    const [postfix, setPostfix] = useState(false)
    const [query, setQuery] = useState({})
    const [isLoaded, setIsLoaded] = useState(false);

    const dispatch = useDispatch();
    const location = useLocation();
    // console.log(isLoaded)
    useEffect(() => {
        const pageDisplayInfo = slidingWindowPages(pageNums, page);
        setDisplayPageNums(pageDisplayInfo.pages)
        setPrefix(pageDisplayInfo.prefix)
        setPostfix(pageDisplayInfo.postfix)
    }, [page, pageNums])

    useEffect(() => {
        setIsLoaded(false)
        const query = {};
        const acceptedParams = new Set([
            "q",
            "minPrice",
            "maxPrice",
            "sellerId",
            "pageSize",
            "page"
        ]);

        if (isSearch) {
            // console.log("WE SEARCHIN")
            const params = new URLSearchParams(location.search)

            if (params.get("page")) {
                setPage(Number(params.get("page")));
            } else if (page !== 1) {
                setPage(1);
            }

            const newPageNums = Array.from({ length: Math.ceil(numResults / (params.get("pageSize") || 20)) }, (_, i) => i + 1)

            if (String(newPageNums) !== String(pageNums)) {
                setPageNums(newPageNums)
            }

            for (let [key, val] of params) {
                if (acceptedParams.has(key)) {
                    if (["page", "pageSize", "sellerId"].includes(key)) {
                        query[key] = Math.floor(val)
                    }
                    else if (key !== 'q') {
                        query[key] = Number(val)

                    } else {
                        query[key] = val
                    }
                }
            }
            setQuery(query)
        } else {
            // console.log(randomPage)
            query.page = randomPage
            query.pageSize = 12
        }

        dispatch(getProducts(query)).then(() => setIsLoaded(true))
    }, [location, dispatch, isSearch, page, pageNums, randomPage])


    return (
        <>
            {!isSearch &&
                <div className="mainpage-top-bar">
                    <div className="mainpage-top-bar-header"><h2>Welcome to Petsy</h2></div>
                    <div className="mainpage-top-bar-categories-wrapper">
                        <NavLink className='mainpage-top-bar-category' to="/search?q=dog">
                            <img alt="dog category" src="https://petsy-project.s3.amazonaws.com/c157526e838c447b8e86077181e5bd70.jpg" />
                            <h3>Dogs</h3>
                        </NavLink>
                        <NavLink className='mainpage-top-bar-category' to="/search?q=cat">
                            <img alt="cat category" src="https://petsy-project.s3.amazonaws.com/d2612064bb974fb4af66d20767613506.jpg" />
                            <h3>Cats</h3>
                        </NavLink>
                        <NavLink className='mainpage-top-bar-category' to="/search?q=bird+parrot">
                            <img alt="bird category" src="https://petsy-project.s3.amazonaws.com/45bbda3ee18b49bf99c577c4535b9f4a.jpg" />
                            <h3>Birds</h3>
                        </NavLink>
                        <NavLink className='mainpage-top-bar-category' to="/search?q=treats+food">
                            <img alt="treat category" src="https://petsy-project.s3.amazonaws.com/1c930544b78a44b5b4d48be35e1de1a6.jpg" />
                            <h3>Treats</h3>
                        </NavLink>
                        <NavLink className='mainpage-top-bar-category' to="/search?q=jacket+robe+costume+hoodie">
                            <img alt="cloathing category" src="https://petsy-project.s3.amazonaws.com/a9aaadc7885c4db5af4a52280934a3cd.jpg" />
                            <h3>Clothes</h3>
                        </NavLink>
                    </div>
                </div>}
            {/* {!isSearch && <h3 className="featured-items">Featured items</h3>} */}
            {isLoaded && (Object.entries(products).length > 1 &&
                <ul id="products-container-products-container">
                    {
                        Object.entries(products).map(([id, product]) => {
                            if (id !== "numResults") {
                                return <Product key={id} product={product} id={id} />
                            }
                            else return null
                        })
                    }
                </ul>)
            }
            {isLoaded && !(Object.entries(products).length > 1) && <div className="products-container-no-results"><h1 ><i className="fa-solid fa-bone"></i><span className="products-container-no-results-message">no results</span><i className="fa-solid fa-bone"></i></h1> <img alt="sad dog" src="https://i.pinimg.com/564x/2d/37/ab/2d37ab595697d54c61094894cdbca161.jpg" /></div>
            }            {
                isSearch && isLoaded &&
                <div className="products-container-navlinks">
                    {prefix && <span className="products-container-dots-before">...</span>}
                    {
                        displayPageNums.map(pageNum =>
                            <NavLink
                                className={`products-container-navlink ${pageNum === page ? "current" : ""}`}
                                key={pageNum}
                                onClick={() => { setPage(pageNum) }}
                                to={`/search?${new URLSearchParams({ ...query, page: pageNum }).toString()}`}
                            >
                                {pageNum}
                            </NavLink>
                        )
                    }
                    {postfix && <span className="products-container-dots-after">...</span>}
                </div>
            }
            {isLoaded && (
                <h6 className="about-links-footer">
                    <div className="about-links-github-icon"> <a href="https://github.com/jhpremo/Petsy-group-project"><i className="fa-brands fa-github" /></a></div>
                    <div className="about-links-creators">Website clone created by <a href="https://github.com/cgalang9">Carmelino Galang</a>, <a href="https://github.com/jhpremo">Jason Premo</a>, <a href="https://github.com/jwad96">Jwad Aziz</a>, and <a href="https://github.com/DevSPK">Sean Kennedy</a></div>
                </h6>)}
        </>
    )

}
