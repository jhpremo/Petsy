export default function slidingWindowPages(pages, page) {
    if (pages.length <= 8) {
      return { pages, page, prefix: false, postfix: false };
    }
  
    let prefix = page > 4;
    let postfix = page < pages.length - 4;
    let subPages;
  
    if (prefix && postfix) {
      subPages = pages.slice(page - 4, page + 4);
    } else if (prefix) {
      subPages = pages.slice(pages.length - 8, pages.length);
    } else {
      subPages = pages.slice(0, 8);
    }
  
    return {
      page,
      prefix,
      postfix,
      pages: subPages,
    };
  }
