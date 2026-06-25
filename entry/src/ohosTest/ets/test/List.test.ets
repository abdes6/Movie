import abilityTest from './Ability.test';
import networkConnectivityTest from './NetworkConnectivity.test';

export default function testsuite() {
  abilityTest();
  networkConnectivityTest();
}
