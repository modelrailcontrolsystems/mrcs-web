/*
Created on 1 Feb 2026

@author: @dcode-software, Bruno Beloff (bbeloff@me.com)

A datetime interval timer
*/

import {useEffect, useState} from "react";

// -------------------------------------------------------------------------------------------------------------------

export const useLiveDate = () => {
    // console.log('useLiveDate')
    const [now, setNow] = useState(new Date());

    useEffect(() => {
        const interval = setInterval(() => {
            setNow(new Date());
        }, 1000);

        return () => clearInterval(interval)
    }, []);

    return now;
};
