import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useLocation, NavLink } from "react-router-dom";
import { getProducts } from "../../../store/items";
import Product from "../Product/Product";
import slidingWindowPages from "./utils/slidingWindowPages"

import "./ProductsContainer.css";

export default function ProductsContainer({ isSearch }) {
    const [numResults, products] = useSelector(state => [state.items.numResults, state.items])

    const [page, setPage] = useState(1);
    const [pageNums, setPageNums] = useState([])
    const [displayPageNums, setDisplayPageNums] = useState([])
    const [prefix, setPrefix] = useState(false)
    const [postfix, setPostfix] = useState(false)
    const [query, setQuery] = useState({})
    const [isLoaded, setIsLoaded] = useState(false);

    const dispatch = useDispatch();
    const location = useLocation();

    useEffect(() => {
        const pageDisplayInfo = slidingWindowPages(pageNums, page);
        setDisplayPageNums(pageDisplayInfo.pages)
        setPrefix(pageDisplayInfo.prefix)
        setPostfix(pageDisplayInfo.postfix)
    }, [page, pageNums])

    useEffect(() => {
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
        }

        dispatch(getProducts(query)).then(() => setIsLoaded(true))

    }, [location, numResults])


    return (
        <>
            {isLoaded && (Object.entries(products).length > 1 &&
                <ul id="products-container-products-container">
                    {
                        Object.entries(products).map(([id, product]) => {
                            if (id !== "numResults") {
                                return <Product key={id} product={product} id={id} />
                            }
                        })
                    }
                </ul> || <div className="products-container-no-results"><h1 ><i className="fa-solid fa-bone"></i><span className="products-container-no-results-message">no results</span><i className="fa-solid fa-bone"></i></h1> <img src="https://i.pinimg.com/564x/2d/37/ab/2d37ab595697d54c61094894cdbca161.jpg" /></div>)
            }
            {
                isSearch &&
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
