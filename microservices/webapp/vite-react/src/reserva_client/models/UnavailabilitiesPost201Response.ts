/* tslint:disable */
/* eslint-disable */
/**
 * Main API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { Unavailability } from './Unavailability';
import {
    UnavailabilityFromJSON,
    UnavailabilityFromJSONTyped,
    UnavailabilityToJSON,
} from './Unavailability';

/**
 * 
 * @export
 * @interface UnavailabilitiesPost201Response
 */
export interface UnavailabilitiesPost201Response {
    /**
     * 
     * @type {Unavailability}
     * @memberof UnavailabilitiesPost201Response
     */
    unavailability?: Unavailability;
}

/**
 * Check if a given object implements the UnavailabilitiesPost201Response interface.
 */
export function instanceOfUnavailabilitiesPost201Response(value: object): boolean {
    let isInstance = true;

    return isInstance;
}

export function UnavailabilitiesPost201ResponseFromJSON(json: any): UnavailabilitiesPost201Response {
    return UnavailabilitiesPost201ResponseFromJSONTyped(json, false);
}

export function UnavailabilitiesPost201ResponseFromJSONTyped(json: any, ignoreDiscriminator: boolean): UnavailabilitiesPost201Response {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'unavailability': !exists(json, 'unavailability') ? undefined : UnavailabilityFromJSON(json['unavailability']),
    };
}

export function UnavailabilitiesPost201ResponseToJSON(value?: UnavailabilitiesPost201Response | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'unavailability': UnavailabilityToJSON(value.unavailability),
    };
}

