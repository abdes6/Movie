import abilityTest from './Ability.test';
import networkConnectivityTest from './NetworkConnectivity.test';
import networkDiagnoseTest from './NetworkDiagnose.test';

export default function testsuite() {
  abilityTest();
  networkConnectivityTest();
  networkDiagnoseTest();
}
