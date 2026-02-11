/*
Created on 1 Feb 2026

@author: @dcode-software, Bruno Beloff (bbeloff@me.com)

A datetime display component

https://www.youtube.com/watch?v=Vz4uwGYGl0E
*/

import {useLiveDate} from "../hooks/useLiveDate.ts";
import styles from "./Clock.module.css"

// -------------------------------------------------------------------------------------------------------------------

const daysOfWeek = [
    'Sun',
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
    'Sat',
    'Sun',
]

const monthsOfYear = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
]

function formattedDateTime(date: Date) {
    // console.log('formattedDateTime - date:', date)

    const dayOfWeek = daysOfWeek[date.getDay()]
    const dayOfMonth = date.getDate().toString().padStart(2, '0')
    const month = monthsOfYear[date.getMonth()]
    const year = date.getFullYear()
    const hours = date.getHours().toString().padStart(2, '0')
    const minutes = date.getMinutes().toString().padStart(2, '0')
    const seconds = date.getSeconds().toString().padStart(2, '0')

    // TODO: time zone

    return `${dayOfWeek} ${dayOfMonth} ${month} ${year} ${hours}:${minutes}:${seconds}`
}

// -------------------------------------------------------------------------------------------------------------------

export const Clock = () => {
    // console.log('Clock')
    const now = useLiveDate();

    return (
        <div className={styles.clock}>
            <b>{formattedDateTime(now)}</b>
        </div>
    )
}
